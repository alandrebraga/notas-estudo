#Set Theory 

** Definicão ** 

Um conjunto deve ser considerado como uma unica entidade, o foco deve ser na colecão de objetos em oposicão a objetos individuais.


Devemos pensar, por exemplo, que um conjunto de empregados como um todo ao invés de um empregado.


** Distinct ** 

A palavra *distinct* siginifica que todos os elementos de um conjunto precisam ser unicos. Indo para tabelas em um banco de dados, podemos forçar isso adotando key constraints, sem uma chave não é possível identificar de forma unica as linhas,e portanto a tabela não se qualifica como um conjunto, ao invés disso, a tabela seria um multiset ou bag.

** Percepcão ** 

A percepcão sobre um conjunto pode ser algo subjetivo, enquanto em uma sala de aula uma pessoa pode pensar como conjunto de pessoas outra pessoa pode pensar como um conjunto de estudantes e um conjunto de professores. No desenvolvimento de um modelo de dados, precisamos sempre considera restes casos subjetivos baseados na necessidade da aplicacão para determinar qual a definicão adequada do conjunto de entidades envolvidas.

A ordem adotada em um conjunto não é importante, a notacão formal para listar um conjunto de elemtos é usado chanves:  
{a, b, c} ou {b, a, c}, já que a ordem não tem relevancia podemos expressar esse conjunto em mais de uma forma. 

Similarmente, temos conjunto de tuplas (linhas no sql) que faz o corpo da relacão, um elemento que é identificado pela suas chaves e não pela posicão.

Quando vamos fazer um modelo de dados, podemos começar identificando quais proposicões precisamos representar. Uma proposicão é uma afirmacão que precisa ser verdadeiro ou falso, um exemplo seria "O empregado andre nasceu em 27 de Janeiro de 1999. E trabalha como analista de dados", isto seria uma proposicão, se for verdadeiro vai ser manifestado como uma linha em uma tabela, se for falsa, simplesmente não há manifestacão.


## Normalizacão

Normalizacão é um processo formal matemático para garantir que a entidade será repsentada por uma única relacão. A normalziacão de bases de dados ajuda a evitar anomalias durante a modificacão de dados e mander a redundancia no minimo possível.

### 1FN

A primeira normal formal define que tuplas (linhas) na relacão (tabela) precisam ser unicas e seis atribudos devem ser atómicos. Em outras palavras seria, se a tabela representa uma relacão, então já esta na primeira normal formal.

A atomicidade de um atribudo é subjetiva, assim como a definicão de conjuntos. Em um exemplo seria relacão de nome da pessoa na tabela Pessoa, o nome poderia ser expresso como um atributo (nome completo), dois atributos (primeiro nome e ultimo nome) ou três atributos (primeiro nome, nome do meio e ultimo nome), o que definirá isso serão os requisitos da aplicacão.



### 2FN

Para atender a segunda norma formal, precisamos primeiro atender a primeira norma formal. Além disso, para estar na 2FN todos os atributos não chaves precisam e devem depender unicamente da chave primária (não podendo depender apenas da parte dela), para aplicara 2FN devemos verificar quais colunas não são funcionalmente dependente da chave primária da tablela e após isso criar uma nova tabela com estes dados.

Exemplo:
    Pedidos = {**orderid**, **productid**, orderdate, qty, customerid, companyname}

Essa tabela violaria a 2FN por conta de que os atributos não chaves dependedem apenas da chave primaria orderid.

Para colocar essa estrutura na segunda normal formal, devemos separar em duas relacões.

Pedidos = {**orderid**, orderdate, customerid, companyname}
OrderDetails = {**productid**, **fk1_orderid**, qty}


### 3FN

Para terceira norma, primeiro precisamos atender a segunda norma. Também devemos entender que, todos os atributos não chaves devem depender de suas chaves candidatas, significando que, todos atributos não chaves devem ser mutualmente independentes. 

No exemplo acima não seguimos a 3FN, já que, customerId e companyName também são dependentes um do outro, para atender esta norma podemos então transforma-lo da seguinte forma.

Pedidos = {**orderid**, orderdate, customerid}
OrderDetails = {**productid**, **fk1_orderid**, qty}
Customers = {**customerid**, companyName}