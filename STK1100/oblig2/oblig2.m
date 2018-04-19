n = 1e4;
U = unifrnd(0,1,[1,n]);

kappa = 4e5;
theta = 3;

X = kappa./((1-U).^(1/theta));
fprintf("mean = %i\n", mean(X));
fprintf("median = %i\n", median(X));

histogram(X, 100, 'BinLimits', [kappa,kappa*5], 'Normalization', 'pdf');
hold on

X2 = linspace(kappa, kappa*5);
Y2 = pareto(X2, theta, kappa);

line(X2, Y2, 'Color', 'red');

xlabel('Income');
ylabel('Probability Density');
legend('Generated Incomes','Pareto-distribution');
%{
mean = 5.982161e+05
median = 5.047831e+05
%}