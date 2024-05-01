x = randn(1, 1000);
window_size = 20;
energies = [];
for k = 1:(length(x) / window_size)
    start_index = (k - 1) * window_size + 1;
    end_index = k * window_size;
    window_energy = sum(x(start_index:end_index).^2);
    energies = [energies, window_energy];
end
plot(energies);
xlabel('Window Index (k)');
ylabel('Energy (E[k])');
title('Energy for every 20 amplitudes');
grid on;
