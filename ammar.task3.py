

def unique_in_order(values):
    """إزالة العناصر المكررة مع الاحتفاظ بالظهور الأول."""
    seen = set()
    return [x for x in values if not (x in seen or seen.add(x))]

print("unique_in_order:", unique_in_order([3, 1, 3, 2, 1]))


def word_frequencies(text):
    """حساب تكرار الكلمات في النص بعد تنظيفها."""
    freq = {}
    for word in text.split():
        cleaned = word.strip(".,;:!?").lower()
        if cleaned:
            freq[cleaned] = freq.get(cleaned, 0) + 1
    return freq

print("word_frequencies:", word_frequencies("The cat. the HAT!"))


def top_k(frequencies, k):
    """أكثر k كلمات تكراراً مرتبة تنازلياً ثم أبجدياً."""
    return sorted(frequencies.items(), key=lambda x: (-x[1], x[0]))[:k]

print("top_k:", top_k({"b": 2, "a": 2, "c": 5}, 2))


def transpose(matrix):
    """تبديل الصفوف والأعمدة للمصفوفة."""
    if not matrix:
        return []
    return [[matrix[r][c] for r in range(len(matrix))] for c in range(len(matrix[0]))]

print("transpose:", transpose([[1, 2, 3], [4, 5, 6]]))


def invert(mapping):
    """عكس المفاتيح والقيم وتجميع المفاتيح المتشابهة مرتبة."""
    inv = {}
    for k, v in mapping.items():
        inv.setdefault(v, []).append(k)
    return {v: sorted(k_list) for v, k_list in inv.items()}

print("invert:", invert({"a": 1, "b": 2, "c": 1}))


def common_elements(first, second):
    """العناصر المميزة المشتركة بين قائمتين مرتبة."""
    return sorted(list(set(first) & set(second)))

print("common_elements:", common_elements([3, 1, 2, 3], [3, 4, 1]))


def group_by_length(words):
    """تجميع الكلمات حسب الطول بنفس ترتيب الإدخال."""
    grouped = {}
    for w in words:
        grouped.setdefault(len(w), []).append(w)
    return grouped

print("group_by_length:", group_by_length(["hi", "sun", "to", "sky"]))


# -- 2. فئة الحقيبة (Bag ADT) 🎒 --

class Bag:
    def __init__(self, items=()):
        self.counts = {}
        for item in items:
            self.add(item)

    def add(self, item):
        self.counts[item] = self.counts.get(item, 0) + 1

    def remove(self, item):
        if item not in self.counts:
            raise KeyError(item)
        self.counts[item] -= 1
        if self.counts[item] == 0:
            del self.counts[item]

    def count(self, item):
        return self.counts.get(item, 0)

    def distinct(self):
        return len(self.counts)

    def __len__(self):
        return sum(self.counts.values())

    def __contains__(self, item):
        return item in self.counts

    def __iter__(self):
        for item in sorted(self.counts.keys()):
            for _ in range(self.counts[item]):
                yield item

    def __eq__(self, other):
        return isinstance(other, Bag) and self.counts == other.counts

    def __repr__(self):
        return f"Bag({list(self)!r})"

b = Bag(["a", "b", "a"])
print("Bag len:", len(b))
print("Bag count 'a':", b.count("a"))
print("Is 'b' in Bag:", "b" in b)
print("Bag distinct items:", b.distinct())
print("Bag representation:", repr(b))


# -- 3. المولدات (Generators) ⚙️ --

def countdown(n):
    """توليد الأرقام تنازلياً من n إلى 1."""
    while n >= 1:
        yield n
        n -= 1

print("countdown:", list(countdown(3)))


def chunks(values, size):
    """تقسيم القائمة إلى شرائح متتالية بالحجم المحدد."""
    if size < 1:
        raise ValueError("Size must be at least 1")
    for i in range(0, len(values), size):
        yield values[i:i+size]

print("chunks:", list(chunks([1, 2, 3, 4, 5], 2)))