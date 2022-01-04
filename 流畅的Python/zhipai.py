import collections

# 实现特定目标的容器，作为Python内建容器的替代
# Counter：字典的子类，提供了可哈希对象的计数功能
# defaultdict：字典的子类，提供了一个工厂函数，为字典查询提供了默认值
# OrderedDict：字典的子类，保留了他们被添加的顺序
# namedtuple：创建命名元组子类的工厂函数
# deque：类似列表容器，实现了在两端快速添加(append)和弹出(pop)
# ChainMap：类似字典的容器类，将多个映射集合到一个视图里面
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]