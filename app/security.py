from passlib.context import CryptContext

# Configuração do contexto de criptografia utilizando estritamente o algoritmo BCrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def gerar_senha_hash(senha: str) -> str:
    """ Aplica o salgamento (salt) aleatório nativo e gera o hash robusto 
    unidirecional e não-reversível a partir da senha fornecida. """
    return pwd_context.hash(senha)

def verificar_senha(senha_pura: str, senha_hash: str) -> bool:
    """ Compara a senha digitada pelo usuário com o hash guardado no banco
    de dados para validar o acesso do profissional à área restrita. """
    return pwd_context.verify(senha_pura, senha_hash)
