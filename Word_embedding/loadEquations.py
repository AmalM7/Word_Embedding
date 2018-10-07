
def load_equations(path):
    with open(path, encoding="utf8") as f :
        lines = f.read()
        lines = lines.split('\n')
        inputs = []
        targets= []
        for line in lines :
            data = line.split('\t')
            if(len(data) == 2):
                inputs.append(data[0])
                targets.append(int(data[1]))
    return (inputs,targets)

if __name__ == '__main__':
    print(load_equations('./equations.txt'))
