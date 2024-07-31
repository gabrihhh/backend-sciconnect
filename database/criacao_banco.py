import mysql.connector

def criar_tabelas(mycursor):
    # Cria a tabela Tipo_Usuario
    mycursor.execute("""
        CREATE TABLE tipo_usuario (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL
        );
    """)
    print("Tabela de tipo_usuario foi criada.")

    # Cria a tabela Usuario
    mycursor.execute("""
        CREATE TABLE usuario (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome_inteiro VARCHAR(255) NOT NULL,
            nome_usuario VARCHAR(255) UNIQUE NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            senha VARCHAR(255) NOT NULL,
            tipo INT,
            FOREIGN KEY (tipo) REFERENCES tipo_usuario(id)
        );
    """)
    print("Tabela de usuários foi criada.")

    # Cria a tabela Artigo
    mycursor.execute("""
        CREATE TABLE artigo (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo TEXT,
            resumo TEXT,
            introducao TEXT,
            metodos TEXT,
            resultados TEXT,
            discussao TEXT,
            conclusao TEXT,
            referencias TEXT,
            agradecimentos TEXT,
            informacao_adicional TEXT,
            usuario_id INT,
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
    """)
    print("Tabela de artigos foi criada.")

    # Cria a tabela Especie
    mycursor.execute("""
        CREATE TABLE especie (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo TEXT,
            descricao TEXT,
            contexto_importancia TEXT,
            objetivo_artigo TEXT,
            classificacao_taxonomica TEXT,
            descricao_classificacao TEXT,
            reino TEXT,
            filo TEXT,
            classe TEXT,
            ordem TEXT,
            familia TEXT,
            genero TEXT,
            especie TEXT,
            descricao_especie TEXT,
            caracteristica_morfologica TEXT,
            caracteristica_fisiologicas TEXT,
            caracteristica_comportamental TEXT,
            distribuicao_geografica TEXT,
            habitat TEXT,
            dieta_alimentacao TEXT,
            predadores_presas TEXT,
            papel_ecologico TEXT,
            descricao_processo_reprodutivo TEXT,
            metodo_reproducao TEXT,
            ciclo_vida TEXT,
            cuidados_parentais TEXT,
            estado_conservacao_especie TEXT,
            interacoes_humanos TEXT,
            bibliografia TEXT,
            usuario_id INT,
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
    """)
    print("Tabela de especies foi criada.")

def popular_tabelas(mycursor):
    # Popula a tabela Tipo_Usuario
    mycursor.execute("INSERT INTO tipo_usuario (nome) VALUES ('Normal');")
    mycursor.execute("INSERT INTO tipo_usuario (nome) VALUES ('Colaborador');")
    print("Tabela de tipo_usuario foi populada.")

    # Popula a tabela Usuario
    mycursor.execute("""
        INSERT INTO usuario (nome_inteiro, nome_usuario, email, senha, tipo) VALUES
        ('João Silva', 'joaos', 'joao@example.com', 'senha123', 1),
        ('Maria Oliveira', 'mariao', 'maria@example.com', 'senha123', 2);
    """)
    print("Tabela de usuários foi populada.")

    # Popula a tabela Artigo
    mycursor.execute("""
        INSERT INTO artigo (titulo, resumo, introducao, metodos, resultados, discussao, conclusao, referencias, agradecimentos, informacao_adicional, usuario_id) VALUES
        ('Estudo sobre a Flora', 'Resumo do estudo', 'Introdução do estudo', 'Métodos do estudo', 'Resultados do estudo', 'Discussão do estudo', 'Conclusão do estudo', 'Referências do estudo', 'Agradecimentos do estudo', 'Informação adicional do estudo', 1),
        ('Pesquisa sobre a Fauna', 'Resumo da pesquisa', 'Introdução da pesquisa', 'Métodos da pesquisa', 'Resultados da pesquisa', 'Discussão da pesquisa', 'Conclusão da pesquisa', 'Referências da pesquisa', 'Agradecimentos da pesquisa', 'Informação adicional da pesquisa', 2);
    """)
    print("Tabela de artigos foi populada.")

    # Popula a tabela Especie
    mycursor.execute("""
        INSERT INTO especie (titulo, descricao, contexto_importancia, objetivo_artigo, classificacao_taxonomica, descricao_classificacao, reino, filo, classe, ordem, familia, genero, especie, descricao_especie, caracteristica_morfologica, caracteristica_fisiologicas, caracteristica_comportamental, distribuicao_geografica, habitat, dieta_alimentacao, predadores_presas, papel_ecologico, descricao_processo_reprodutivo, metodo_reproducao, ciclo_vida, cuidados_parentais, estado_conservacao_especie, interacoes_humanos, bibliografia, usuario_id) VALUES
        ('Especie A', 'Descrição A', 'Importância A', 'Objetivo A', 'Classificação A', 'Descrição Classificação A', 'Reino A', 'Filo A', 'Classe A', 'Ordem A', 'Família A', 'Gênero A', 'Espécie A', 'Descrição Espécie A', 'Morfologia A', 'Fisiologia A', 'Comportamento A', 'Distribuição A', 'Habitat A', 'Dieta A', 'Predadores A', 'Papel Ecológico A', 'Reprodução A', 'Método Reprodução A', 'Ciclo de Vida A', 'Cuidados Parentais A', 'Conservação A', 'Interações Humanos A', 'Bibliografia A', 1),
        ('Especie B', 'Descrição B', 'Importância B', 'Objetivo B', 'Classificação B', 'Descrição Classificação B', 'Reino B', 'Filo B', 'Classe B', 'Ordem B', 'Família B', 'Gênero B', 'Espécie B', 'Descrição Espécie B', 'Morfologia B', 'Fisiologia B', 'Comportamento B', 'Distribuição B', 'Habitat B', 'Dieta B', 'Predadores B', 'Papel Ecológico B', 'Reprodução B', 'Método Reprodução B', 'Ciclo de Vida B', 'Cuidados Parentais B', 'Conservação B', 'Interações Humanos B', 'Bibliografia B', 2);
    """)
    print("Tabela de especies foi populada.")

def main():
    # Conectar ao banco de dados
    conn = mysql.connector.connect(
        host="172.17.0.2",
        user="root",
        password="99076641",
        database="sciconnect"
    )
    mycursor = conn.cursor()

    # Verifica se o banco de dados existe
    mycursor.execute("SHOW DATABASES LIKE %s", ("sciconnect",))
    result = mycursor.fetchone()

    if result:
        # Se o banco de dados existe, apaga-o
        mycursor.execute(f"DROP DATABASE sciconnect;")
        print(f"Banco de dados sciconnect foi apagado.")

    # Cria o banco de dados
    mycursor.execute(f"CREATE DATABASE sciconnect")
    print(f"Banco de dados sciconnect foi criado.")

    # Aponta para o banco de dados
    mycursor.execute(f"USE sciconnect")
    print(f"Apontando para o banco de dados.")

    # Criar as tabelas
    criar_tabelas(mycursor)

    # Commit das transações
    conn.commit()

    # Popular as tabelas
    while True:
        resposta = input("Quer deixar as tabelas populadas? (Y)").strip().upper()

        if resposta == 'Y':
            popular_tabelas(mycursor)
            break
        elif resposta == '':
            popular_tabelas(mycursor)
            break
        elif resposta == 'N':
            print("Operação cancelada!")
            break
        else:
            print("Entrada inválida. Por favor, digite 'Y' ou 'N'.")
    

    # Commit das transações
    conn.commit()

    # Fechar a conexão
    mycursor.close()
    conn.close()

if __name__ == "__main__":
    main()
