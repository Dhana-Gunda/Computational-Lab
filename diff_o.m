% Define the differential equation dy/dt = f(t, y)
function dydt = myODE(t, y)
    dydt = -0.5 * y; % Example: -0.5*y represents a simple exponential decay
endfunction

% Define the time span
tspan = [0, 10];

% Define the initial condition
y0 = 1;

% Solve the differential equation
[t, y] = ode45(@myODE, tspan, y0);

% Plot the solution
plot(t, y);
xlabel('Time');
ylabel('y(t)');
title('Solution of the Differential Equation');