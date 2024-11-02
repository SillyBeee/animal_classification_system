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
        print(f"Adding fact: {fact}")  # 调试输出
        self.database.append(fact)

    def infer(self):
        while True:
            applicable_knowledge = self.find_applicable_knowledge()
            if not applicable_knowledge:
                break
            for knowledge in applicable_knowledge:
                self.apply_knowledge(knowledge)

    def find_applicable_knowledge(self):
        applicable_knowledge = []
        for knowledge in self.knowledge_base:
            if all(fact in self.database for fact in knowledge["if"]):
                applicable_knowledge.append(knowledge)
        # print(f"Applicable knowledge: {applicable_knowledge}")  # 调试输出
        return applicable_knowledge

    def apply_knowledge(self, knowledge):
        if knowledge["then"] not in self.database:
            # print(f"Applying knowledge: {knowledge}")  # 调试输出
            self.database.append(knowledge["then"])

    def classify(self):
        self.infer()
        result = [fact for fact in self.database if fact in ["老虎", "金钱豹", "斑马", "长颈鹿", "鸵鸟", "企鹅", "信天翁"]]
        print(f"Classification result: {result}")  # 调试输出
        return result

# Example usage
if __name__ == "__main__":
    system = AnimalClassificationSystem()
    while True:
        fact = input("请输入一个特征 (输入 '结束' 以停止): ")
        if fact == "结束":
            break
        system.add_fact(fact)
    result = system.classify()
    print("识别出的动物:", result)