from llama_index.core import SimpleDirectoryReader
from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import StorageContext, VectorStoreIndex
from llama_index.vector_stores.pinecone import PineconeVectorStore
from core.database import create_index
from core.chat_engine import get_chat_engine
from core.add_summary import add_summary
import os


def build_index():
    
   Settings.embed_model = HuggingFaceEmbedding(model_name='intfloat/multilingual-e5-small')

   
   BASE_DIR = os.path.dirname(os.path.abspath(__file__))
   pdf_path = os.path.join(BASE_DIR, 'files', 'Tese_Suzart _ Lingua_Kariri_Xoco_178_197.pdf')


   
   # Carregar os documentos 
   documents = SimpleDirectoryReader(input_files=[pdf_path], file_extractor={".pdf": PDFReader()}).load_data()
   
   documents.append(add_summary())
   print("Documentos carregados com sucesso")
   

   
   
   # Dividindo em chunks
   node_parser = SentenceSplitter(chunk_size=1000, chunk_overlap=200) # Cada chunk pode ter no máximo 1000 tokens 
   nodes = node_parser.get_nodes_from_documents(documents)
   print("Chunks criados com sucesso")

   
   
   # Criando o index no projeto
   pc = create_index()
   
   pinecone_index = pc.Index("kariri-xoco")
   print("Index criado e pego com sucesso")

   
   
   # Criando Vector store
   vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
   storage_context = StorageContext.from_defaults(vector_store=vector_store)
   print("Vector store criado com sucesso")

   
   
   # Criando os embeddings e colocando no banco
   VectorStoreIndex(nodes, storage_context=storage_context)
   print("Embeddings criados e colocados no banco com sucesso")
   
   
build_index()