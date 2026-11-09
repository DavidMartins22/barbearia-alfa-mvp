import pytest
from app.security import gerar_senha_hash, verificar_senha

def test_deve_gerar_hash_inverssivel_e_seguro():
    """ Teste Unitário: Garante que o algoritmo BCrypt está gerando hashes 
    unidirecionais válidos e que a senha pura original não fica legível. """
    senha_teste = "marcus_alfa_2026"
    
    hash_gerado = gerar_senha_hash(senha_teste)
    
    # O hash gerado obrigatoriamente deve ser diferente da senha em texto limpo
    assert hash_gerado != senha_teste
    # Garante que o BCrypt aplicou o padrão estrutural robusto correto
    assert hash_gerado.startswith("$2b$") or hash_gerado.startswith("$2a$")

def test_deve_validar_credenciais_corretas_e_rejeitar_invalidas():
    """ Teste Unitário: Comprova que o sistema autentica com sucesso a credencial
    verdadeira e barra tentativas com senhas incorretas. """
    senha_correta = "senha_secreta_123"
    senha_errada = "tentativa_maliciosa"
    
    hash_referencia = gerar_senha_hash(senha_correta)
    
    # 1. Caso de sucesso: A senha digitada confere com o hash do banco
    assert verificar_senha(senha_correta, hash_referencia) is True
    
    # 2. Caso de falha: Uma senha incorreta deve ser categoricamente rejeitada
    assert verificar_senha(senha_errada, hash_referencia) is False
