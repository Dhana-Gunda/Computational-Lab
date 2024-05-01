t = 0:0.01:2*pi;
y1 = sin(t);
y2 = cos(t);
y3 = sin(3*t);
y4 = cos(2*t);

subplot(2, 2, 1);
plot(t, y1);
title('sin(t)');

subplot(2, 2, 2);
plot(t, y2);
title('cos(t)');

subplot(2, 2, 3);
plot(t, y3);
title('sin(3t)');

subplot(2, 2, 4);
plot(t, y4);
title('cos(2t)');