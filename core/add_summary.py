from llama_index.core import Document


def add_summary():
    
    metadata_doc = Document(
        
        text=(
            
            """ 
    --- RESUMO PADRÃO (CONTEXTO INTERNO) ---
    O documento apresenta um glossário/lexicão cultural do povo indígena Kariri-Xocó (da Terra Indígena Kariri-Xocó, em Porto Real do Colégio - AL), focado em dois eixos principais:

    1. Cerâmica (Louça Utilitária e Ancestral):
    Detalha o processo de confecção artesanal e ancestral da cerâmica, majoritariamente realizado pelas mulheres (ceramistas/louceiras) e transmitido via tradição oral. Descreve as matérias-primas (diferentes tipos de barro/argila como o barro marrom, vermelho, tauá amarelo e tauá branco; areia; cinzas), as ferramentas e recipientes artesanais (balaio, caçuá, capeador/coité, sabugo de milho, semente de mucunã), bem como os processos de modelagem, alisamento, pintura floral/geométrica, secagem ao sol e queima em forno a lenha (com apoio dos homens no transporte de lenha e na etapa de estoquear/queimar). Destaca utensílios como potes, talhas, moringas, igaçabas (porrões), panelas, cuscuzeiras, fogareiros e brinquedos de barro, além da importância histórica e econômica das trocas e da "canoa do pote" pelo Rio São Francisco (Opará).

    2. Pintura Corporal e Artesanal:
    Aborda os aspectos simbólicos, espirituais, sociais e cosmológicos do corpo pintado, considerado a "roupa ancestral" e escudo de proteção espiritual/física. Detalha os elementos naturais empregados na preparação das tintas (jenipapo para a cor preta/azul-escura; carvão da imburana-de-cambão; urucum e pedra vermelha para o vermelho; tauá branco e amarelo para o branco e amarelo), bem como as ferramentas utilizadas (pilão, peneira, cuia, talisca de pau e os próprios dedos). Explica o significado das cores, dos adereços/adornos (como os cocares de penas de arara) e dos grafismos (circulares, triangulares/angulares, ondulares e irregulares) aplicados em diferentes partes do corpo (testa, peitoral, costas, antebraço, punho, pernas e canelas) ou em artesanatos, panos e cerâmicas, refletindo a ancestralidade, a divisão de papéis ritualísticos (como no Toré e Ouricuri) e a identidade étnica Kariri-Xocó.
    --- FIM DO RESUMO PADRÃO ---
            """
 
        ),
        metadata={"tipo": "metadados_gerais", "file_name": "resumo_geral.md"}
    )
    
    return metadata_doc
