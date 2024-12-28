% PSO算法求解函数的最小值或最大值
clc; clear; close all;

% 参数设置
pop_size = 30;    % 粒子数
dim = 2;          % 变量维度
max_iter = 100;   % 最大迭代次数
lb = -5;          % 下界
ub = 5;           % 上界
w = 0.7;          % 惯性权重
c1 = 1.5;         % 个体学习因子
c2 = 1.5;         % 群体学习因子

% 初始化粒子群
x = lb + (ub-lb) * rand(pop_size, dim);  % 位置
v = zeros(pop_size, dim);                % 速度
p_best = x;                              % 个体最佳位置
g_best = x(1, :);                        % 全局最佳位置
fitness = @(x1, x2) 15 + x1.^2 + x2.^2 - 10*(cos(2*pi*x1) + cos(2*pi*x2));

% 计算初始适应度
p_best_val = arrayfun(@(i) fitness(x(i, 1), x(i, 2)), 1:pop_size);
[g_best_val, g_best_idx] = min(p_best_val); % 改为max(p_best_val)求最大值
g_best = p_best(g_best_idx, :);

% PSO迭代
for iter = 1:max_iter
    for i = 1:pop_size
        % 更新速度和位置
        r1 = rand; r2 = rand;
        v(i, :) = w * v(i, :) + c1 * r1 * (p_best(i, :) - x(i, :)) + c2 * r2 * (g_best - x(i, :));
        x(i, :) = x(i, :) + v(i, :);

        % 边界处理
        x(i, :) = max(min(x(i, :), ub), lb);

        % 更新个体最佳
        f_val = fitness(x(i, 1), x(i, 2));
        if f_val < p_best_val(i)  % 改为 > 求最大值
            p_best(i, :) = x(i, :);
            p_best_val(i) = f_val;
        end
    end

    % 更新全局最佳
    [current_best_val, current_best_idx] = min(p_best_val); % 改为 max 求最大值
    if current_best_val < g_best_val  % 改为 > 求最大值
        g_best_val = current_best_val;
        g_best = p_best(current_best_idx, :);
    end

    % 输出迭代信息
    fprintf('第%d次迭代: 最优值 = %.4f\n', iter, g_best_val);
end

% 输出结果
fprintf('最优解: x1 = %.4f, x2 = %.4f\n', g_best(1), g_best(2));
fprintf('最优值: %.4f\n', g_best_val);
