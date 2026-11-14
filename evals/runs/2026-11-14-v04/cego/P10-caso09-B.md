[Listei a pasta e testei a extração de texto em 3 amostras: 40 arquivos (31 PDF e 9 Word); 2 PDFs têm texto selecionável e 1 é escaneado, sem camada de texto, então vai precisar de OCR.]

Olhei a pasta: são 40 contratos, 31 em PDF e 9 em Word. Pelas amostras, a maioria extrai texto sem problema. Pelo menos um PDF é imagem escaneada e precisa de OCR. Vou checar quantos são assim antes de confiar nos números.

**Como vou fazer**

1. **Extração em lote, sem modelo.** Converto os 40 arquivos para texto com script e marco quais precisam de OCR ou ficaram ilegíveis. É barato e deixa um texto-fonte para conferir depois.
2. **Um subagente por contrato, em paralelo.** Cada um preenche a mesma ficha, com modelo intermediário e esforço médio: partes, vigência, renovação automática, prazo de aviso para rescisão, prazos de pagamento e entrega, multas (rescisão, atraso, SLA), limite de responsabilidade, reajuste, exclusividade, foro. Cada campo leva a **citação literal e a cláusula**. Se o contrato não disser, o campo fica "não consta" e não recebe um palpite.
3. **Revisão no modelo máximo.** Eu mesmo reviso os contratos com campos vazios, cláusulas ambíguas ou multas fora do padrão. Faço isso porque um erro em multa ou prazo custa caro e é o ponto onde um modelo menor mais erra.
4. **Ranking dos 5 mais arriscados.** A comparação entre os 40 fica comigo, sobre as fichas já conferidas.

**Entrega:** uma planilha com uma linha por contrato (prazos, multas, renovação, alertas), mais um resumo curto com o top 5 e o motivo de cada um.

**Uma decisão sua antes do ranking.** "Mais arriscado" pode significar coisas diferentes, e o top 5 muda conforme o critério:
- **(a) Exposição financeira:** multas altas, responsabilidade ilimitada, reajuste sem teto.
- **(b) Armadilha de prazo:** renovação automática com janela de aviso curta, que você pode perder sem perceber.
- **(c) Dependência operacional:** fornecedor crítico, com exclusividade ou difícil de trocar.

Minha sugestão é combinar os três, com peso maior em (a) e (b), e mostrar a nota de cada critério por contrato para você ver por que cada um entrou. Se algum fornecedor for crítico para o seu negócio, me diga quais. Isso eu não consigo tirar do texto do contrato.

Também vale avisar: isto é uma triagem, não um parecer jurídico. Os 5 do topo devem passar por um advogado antes de você agir.

Já começo a etapa 1 agora, porque ela não depende da sua resposta. Se você não responder sobre o critério, sigo com a combinação (a)+(b)+(c) e deixo o peso ajustável na planilha.
