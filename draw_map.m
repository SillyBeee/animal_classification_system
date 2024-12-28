% 绘制函数三维曲面图和等高线图
clc; clear; close all;

% 定义域
x1 = -5:0.1:5;
x2 = -5:0.1:5;
[X1, X2] = meshgrid(x1, x2);

% 目标函数
F = 15 + X1.^2 + X2.^2 - 10*(cos(2*pi*X1) + cos(2*pi*X2));

% 绘制三维曲面图
figure;
surf(X1, X2, F);
title('三维曲面图');
xlabel('x1'); ylabel('x2'); zlabel('f(x1, x2)');
shading interp; colorbar;

% 绘制二维等高线图
figure;
contour(X1, X2, F, 50); % 50个等高线
title('二维等高线图');
xlabel('x1'); ylabel('x2'); colorbar;
