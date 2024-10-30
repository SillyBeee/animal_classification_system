#pragma once
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>

int print_mode_request( ){
    int mode_=0;
    std::cout<<"请输入您想要运行的推理系统的模式(1:正向推理 2:反向推理):\n"<<std::endl;
    std::cin>>mode_;
    if (mode_!=1&&mode_!=2){
        std::cout<<"输入有误，请重新输入"<<std::endl;
        return print_mode_request();
    }
    else{
        return mode_;
    }
}

std::vector<int> input_request(){
    std::cout<<" 请输入您已知的特征: 1: 有毛发, 2: 有奶, 3: 有羽毛, 4: 会飞, 5: 会下蛋, 6: 吃肉, 7: 有犬齿,
                8: 有爪, 9: 眼盯前方, 10: 有蹄, 11: 是咀嚼反刍动物, 12: 是黄褐色, 13: 身上有暗斑点, 14: 身上有黑色条纹,
                15: 有长脖子, 16: 有长腿, 17: 不会飞, 18: 会游泳, 19: 有黑白二色, 20: 善飞, 21: 是哺乳动物,
                22: 是鸟, 23: 是食肉动物, 24: 是蹄类动物 "<<std::endl;
    
    
}
class rules{
    public: 
    private:
        rule[]
        
}