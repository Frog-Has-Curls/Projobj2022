 program bubblesort;

var
lista : array[integer] of 1..50;

i, flaga, temp: integer;

const n:integer =50;
procedure sort;

begin

flaga := 0;

while flaga = 0 do
    begin
        flaga:=1;
        for i:=1 to n-1 do
            begin
                if lista[i] >lista[i+1] then
                    begin
                        flaga:=0;
                        temp := lista[i];
                        lista[i] := lista[i+1];
                        lista[i+1] :=temp;

                    end;
            end;
 

    end;
end;
begin

for i:=1 to n do
    begin
        lista[i]:=random(n);
        writeln(lista[i]);
    end;

    sort();
    writeln('Posortowane!');

    for i:=1 to n do
        begin
            write (' | ', lista[i]);

        end;

    end.
