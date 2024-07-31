
USE sciconnect;


CREATE TABLE Usuario (
    Id SERIAL PRIMARY KEY,
    Nome_inteiro VARCHAR(255) NOT NULL,
    Nome_usuario VARCHAR(255) UNIQUE NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Senha VARCHAR(255) NOT NULL,
    Tipo INTEGER REFERENCES Tipo_Usuario(Id)
);

CREATE TABLE Tipo_Usuario (
    Id SERIAL PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL
);

CREATE TABLE Artigo (
    Id SERIAL PRIMARY KEY,
    Titulo TEXT,
    Resumo TEXT,
    Introducao TEXT,
    Metodos TEXT,
    Resultados TEXT,
    Discussao TEXT,
    Conclusao TEXT,
    Referencias TEXT,
    Agradecimentos TEXT,
    Informacao_adicional TEXT,
    Usuario_id INTEGER REFERENCES Usuario(Id)
);

CREATE TABLE Especie (
    Id SERIAL PRIMARY KEY,
    Titulo TEXT,
    Descricao TEXT,
    Contexto_importancia TEXT,
    Objetivo_artigo TEXT,
    Classificacao_taxonomica TEXT,
    Descricao_classificacao TEXT,
    Reino TEXT,
    Filo TEXT,
    Classe TEXT,
    Ordem TEXT,
    Familia TEXT,
    Genero TEXT,
    Especie TEXT,
    Descricao_especie TEXT,
    Caracteristica_morfologica TEXT,
    Caracteristica_fisiologicas TEXT,
    Caracteristica_comportamental TEXT,
    Distribuicao_geografica TEXT,
    Habitat TEXT,
    Dieta_alimentacao TEXT,
    Predadores_presas TEXT,
    Papel_ecologico TEXT,
    Descricao_processo_reprodutivo TEXT,
    Metodo_reproducao TEXT,
    Ciclo_vida TEXT,
    Cuidados_parentais TEXT,
    Estado_conservacao_especie TEXT,
    Interacoes_humanos TEXT,
    Bibliografia TEXT,
    Usuario_id INTEGER REFERENCES Usuario(Id)
);

-- Populando a tabela Tipo_Usuario
INSERT INTO Tipo_Usuario (Nome) VALUES ('Normal');
INSERT INTO Tipo_Usuario (Nome) VALUES ('Colaborador');

-- Populando a tabela Usuario
INSERT INTO Usuario (Nome_inteiro, Nome_usuario, Email, Senha, Tipo) VALUES
('Alice Silva', 'alice_silva', 'alice@example.com', 'senha123', 1),
('Bob Santos', 'bob_santos', 'bob@example.com', 'senha123', 2),
('Carol Costa', 'carol_costa', 'carol@example.com', 'senha123', 1),
('David Lima', 'david_lima', 'david@example.com', 'senha123', 2);

-- Populando a tabela Artigo
INSERT INTO Artigo (Titulo, Resumo, Introducao, Metodos, Resultados, Discussao, Conclusao, Referencias, Agradecimentos, Informacao_adicional, Usuario_id) VALUES
('Estudo sobre a fauna local', 'Resumo do estudo sobre a fauna local', 'Introducao do estudo', 'Metodos utilizados no estudo', 'Resultados do estudo', 'Discussao sobre os resultados', 'Conclusao do estudo', 'Referencias utilizadas', 'Agradecimentos aos colaboradores', 'Informacoes adicionais', 1),
('Impacto ambiental na floresta', 'Resumo sobre o impacto ambiental', 'Introducao sobre o impacto ambiental', 'Metodos utilizados para avaliar o impacto', 'Resultados da avaliacao', 'Discussao sobre o impacto', 'Conclusao sobre o impacto ambiental', 'Referencias utilizadas', 'Agradecimentos aos colaboradores', 'Informacoes adicionais', 2);

-- Populando a tabela Especie
INSERT INTO Especie (Titulo, Descricao, Contexto_importancia, Objetivo_artigo, Classificacao_taxonomica, Descricao_classificacao, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Descricao_especie, Caracteristica_morfologica, Caracteristica_fisiologicas, Caracteristica_comportamental, Distribuicao_geografica, Habitat, Dieta_alimentacao, Predadores_presas, Papel_ecologico, Descricao_processo_reprodutivo, Metodo_reproducao, Ciclo_vida, Cuidados_parentais, Estado_conservacao_especie, Interacoes_humanos, Bibliografia, Usuario_id) VALUES
('Estudo sobre a espécie A', 'Descrição da espécie A', 'Importância da espécie A', 'Objetivo do artigo sobre a espécie A', 'Classificação taxonômica da espécie A', 'Descrição da classificação da espécie A', 'Animalia', 'Chordata', 'Mammalia', 'Carnivora', 'Felidae', 'Panthera', 'Panthera leo', 'Descrição do leão', 'Características morfológicas do leão', 'Características fisiológicas do leão', 'Comportamento do leão', 'Distribuição geográfica do leão', 'Habitat do leão', 'Dieta do leão', 'Predadores e presas do leão', 'Papel ecológico do leão', 'Descrição do processo reprodutivo do leão', 'Método de reprodução do leão', 'Ciclo de vida do leão', 'Cuidados parentais do leão', 'Estado de conservação do leão', 'Interações do leão com humanos', 'Bibliografia sobre o leão', 1),
('Estudo sobre a espécie B', 'Descrição da espécie B', 'Importância da espécie B', 'Objetivo do artigo sobre a espécie B', 'Classificação taxonômica da espécie B', 'Descrição da classificação da espécie B', 'Plantae', 'Magnoliophyta', 'Magnoliopsida', 'Rosales', 'Rosaceae', 'Rosa', 'Rosa gallica', 'Descrição da rosa gallica', 'Características morfológicas da rosa gallica', 'Características fisiológicas da rosa gallica', 'Comportamento da rosa gallica', 'Distribuição geográfica da rosa gallica', 'Habitat da rosa gallica', 'Dieta da rosa gallica', 'Predadores e presas da rosa gallica', 'Papel ecológico da rosa gallica', 'Descrição do processo reprodutivo da rosa gallica', 'Método de reprodução da rosa gallica', 'Ciclo de vida da rosa gallica', 'Cuidados parentais da rosa gallica', 'Estado de conservação da rosa gallica', 'Interações da rosa gallica com humanos', 'Bibliografia sobre a rosa gallica', 2);

-- Confirmando as inserções
COMMIT;

