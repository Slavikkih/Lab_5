import networkx as nx


def is_isomorphic(G1, G2):
    """
    Перевірка на ізоморфізм графів G1 та G2.
    Повертає True, якщо графи ізоморфні, і False, якщо ні.
    """
    return nx.is_isomorphic(G1, G2)


def modify_graph(G1, G2):
    """
    Модифікація графу G2 для забезпечення його ізоморфізму з G1.
    Повертає модифікований граф G2.
    """
    # отримати список вузлів G1 та G2
    nodes1 = list(G1.nodes())
    nodes2 = list(G2.nodes())

    # створити відображення між вузлами G1 та G2
    mapping = {}
    for i in range(len(nodes1)):
        mapping[nodes2[i]] = nodes1[i]

    # перенумерувати вузли G2 за відображенням
    G2 = nx.relabel_nodes(G2, mapping)

    # повернути модифікований граф G2
    return G2


# Приклад використання:

# створити графи G1 та G2
G1 = nx.Graph()
G1.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

G2 = nx.Graph()
G2.add_edges_from([(5, 6), (6, 7), (7, 8), (8, 5)])

# перевірити на ізоморфізм та модифікувати G2
if not is_isomorphic(G1, G2):
    G2 = modify_graph(G1, G2)

# перевірити на ізоморфізм ще раз
if is_isomorphic(G1, G2):
    print("Графи G1 та G2 ізоморфні.")
else:
    print("Графи G1 та G2 неізоморфні. Граф G2 було модифіковано.")
    print("Модифікований граф G2:", G2.edges())
