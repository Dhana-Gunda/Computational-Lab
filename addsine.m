x = 0:0.01:10;
x2 = 0:0.02:20;

sin1 = sin(x);
sin2 = sin(x2);

x2 /= 2;

sin3 = sin1 + sin2;

plot(x, sin3);
