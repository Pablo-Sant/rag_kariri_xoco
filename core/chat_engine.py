from llama_index.core import VectorStoreIndex
from core.config_llm import llm
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.pinecone import PineconeVectorStore
from core.database import get_index
from llama_index.core.memory import ChatMemoryBuffer



chat_engine = None
 
system_prompt = (
""" 
Você é um assistente virtual especializado em fornecer informações precisas com base no documento do povo indígena Kariri-Xocó,abordando Cerâmica, Pintura Corporal e Artesanal, religiosidade, família e demais coisas.
INSTRUÇÕES DE COMPORTAMENTO E RESPOSTA:
0. Se a informação não estiver no contexto fornecido, diga explicitamente que não possui essa informação, em vez de inferir ou complementar com conhecimento geral.
1. Sempre responda às dúvidas dos usuários com base estritamente no contexto fornecido do documento.
2. Mantenha um tom respeitoso, informativo e culturalmente sensível ao falar sobre as tradições, saberes ancestrais, cosmologia e práticas do povo Kariri-Xocó.
3. Nunca diga que vc está lendo do resumo se a pergunta for o resumo ou sobre o resumo ou sobre o que o documento fala.
""" 
)
 
 
def get_chat_engine():
    global chat_engine

    if chat_engine is None:
        
        Settings.embed_model = HuggingFaceEmbedding( # É necessário definir aqui, pois a transformação de texto em embedding tbm é usada na produção 
            model_name='intfloat/multilingual-e5-small'
        )
        
       
        pinecone_index = get_index()
         

        vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
        index = VectorStoreIndex.from_vector_store(vector_store)

        chat_engine = index.as_chat_engine(
            llm=llm,
            mode='context',
            similarity_top_k=6,
            system_prompt = system_prompt,
            memory = ChatMemoryBuffer.from_defaults(token_limit=4000)
        )

    return chat_engine