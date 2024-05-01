lx = 50;
ly = 30;
x = randn(1, lx);
y = randn(1, ly);
lz = lx + ly - 1;
z = zeros(1, lz);
for k = 0:2:(lx + ly - 2)
    for n = 0:(lx - 1)
        if (n + k + 1) <= lz
            z(n + k + 1) = z(n + k + 1) + x(n + 1) * y(n + 1);
        end
    end
end
stem(z);
xlabel('n');
ylabel('z[n]');
title('z[n] = \Sigma_{t=0}^{n} x[n]y[n+k]');
