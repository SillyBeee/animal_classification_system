class AnimalClassificationSystem:
    def __init__(self):
        self.knowledge_base = [
            {"if": ["有条纹", "体型大"], "then": "老虎"},
            {"if": ["有斑点", "体型大"], "then": "金钱豹"},
            {"if": ["有条纹", "体型中等"], "then": "斑马"},
            {"if": ["有长脖子"], "then": "长颈鹿"},
            {"if": ["不能飞", "体型大"], "then": "鸵鸟"},
            {"if": ["不能飞", "体型中等"], "then": "企鹅"},
            {"if": ["能飞", "体型大"], "then": "信天翁"}
        ]
        self.database = []

    def add_fact(self, fact):
        if fact not in self.database:
            self.database.append(fact)

    def find_applicable_knowledge(self):
        applicable_knowledge = []
        for knowledge in self.knowledge_base:
            if (all(fact in self.database for fact in knowledge["if"])
                and knowledge["then"] not in self.database):
                applicable_knowledge.append(knowledge)
        return applicable_knowledge

    def apply_knowledge(self, knowledge):
        conclusion = knowledge["then"]
        if conclusion not in self.database:
            self.database.append(conclusion)

    def infer(self):
        while True:
            applicable_rules = self.find_applicable_knowledge()
            if not applicable_rules:
                break
            for rule in applicable_rules:
                self.apply_knowledge(rule)


if __name__ == "__main__":
    system = AnimalClassificationSystem()
    while True:
        fact = input("请输入一个特征(空行结束): ").strip()
        if not fact:
            break
        system.add_fact(fact)
    system.infer()
    print("识别结果:", system.database)