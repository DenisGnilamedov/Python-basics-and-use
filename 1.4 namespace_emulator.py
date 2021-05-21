def create(namesp, parent):
    par_nsp[namesp] = parent
    nsp_var[namesp] = []


def add(namesp, var):
    nsp_var[namesp] = var


def get(namesp, var):
    if var in nsp_var[namesp]:
        return namesp
    elif var not in nsp_var[namesp]:
        if var in par_nsp[namesp]:
            return namesp
        else:
            return


n = int(input())
par_nsp = {'global': 'None'}
nsp_var = {'global': []}
for i in range(n):
    cmd, namespace, arg = input().split()
    if cmd == 'create':
        create(namespace, arg)
    elif cmd == 'add':
        add(namespace, arg)
    elif cmd == 'get':
        get(namespace, arg)
        print(get(namespace, arg))

