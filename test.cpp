#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

// 定义规则结构
struct Rule {
    vector<string> conditions;  // 前提条件
    string conclusion;          // 结论
};

// 动物识别系统类
class AnimalRecognitionSystem {
private:
    vector<Rule> ruleBase;                     // 规则库
    unordered_map<string, bool> factBase;      // 综合数据库

public:
    AnimalRecognitionSystem() {
        // 初始化规则库
        ruleBase = {
            {{"有条纹", "大型猫科动物"}, "虎"},
            {{"有斑点", "大型猫科动物"}, "金钱豹"},
            {{"有条纹", "草原动物"}, "斑马"},
            {{"长脖子", "草原动物"}, "长颈鹿"},
            {{"不会飞", "长腿", "鸟类"}, "鸵鸟"},
            {{"不会飞", "生活在南极", "鸟类"}, "企鹅"},
            {{"会飞", "生活在海洋附近", "鸟类"}, "信天翁"}
        };
    }

    void addFact(const string& fact) {
        factBase[fact] = true;
    }

    void infer() {
        for (const auto& rule : ruleBase) {
            bool match = true;
            for (const auto& condition : rule.conditions) {
                if (factBase.find(condition) == factBase.end() || !factBase[condition]) {
                    match = false;
                    break;
                }
            }
            if (match) {
                cout << "识别结果: " << rule.conclusion << endl;
                return;
            }
        }
        cout << "无法识别该动物。" << endl;
    }
};

int main() {
    AnimalRecognitionSystem system;

    cout << "请输入该动物的特征（输入“完成”结束输入）：" << endl;
    string input;
    while (true) {
        cout << "特征: ";
        cin >> input;
        if (input == "完成") break;
        system.addFact(input);
    }

    // 开始推理
    system.infer();

    return 0;
}
