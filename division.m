x = input("Enter x: ");
y = input("Enter y: ");
if (y != 0)
    if (isa(x, 'double') && isa(y, 'double')) || (isa(x, 'float') && isa(y, 'float')) || (isa(x, 'float') && isa(y, 'double')) || (isa(x, 'double') && isa(y, 'float'))
        disp(x/y);
    end
else
    disp("Division not possible");
end