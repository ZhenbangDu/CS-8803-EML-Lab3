import torch
import time


def check_broadcast(x, a, b, c, d):
    return x.max().item() == a.max().item() == b.max().item() == c.max().item() == d.max().item()


def broadcast1(x, a, b, c, d):
    # For example, use a.copy_(x) to copy the data from x to a
    pass


def broadcast2(x, a, b, c, d):
    pass


def broadcast3(x, a, b, c, d):
    pass

def timeit(boradcast):

    x = torch.randn((100000, 10000))
    a = torch.zeros((100000, 10000), device="cuda:0")
    b = torch.zeros((100000, 10000), device="cuda:1")
    c = torch.zeros((100000, 10000), device="cuda:2")
    d = torch.zeros((100000, 10000), device="cuda:3")


    torch.cuda.synchronize(0)
    torch.cuda.synchronize(1)
    torch.cuda.synchronize(2)
    torch.cuda.synchronize(3)

    tic = time.time()

    boradcast(x, a, b, c, d)

    torch.cuda.synchronize(0)
    torch.cuda.synchronize(1)
    torch.cuda.synchronize(2)
    torch.cuda.synchronize(3)

    toc = time.time()

    assert check_broadcast(x, a, b, c, d)
    return toc - tic


print('Running time for broadcast1:', timeit(broadcast1), '(s)')
print('Running time for broadcast2:', timeit(broadcast2), '(s)')
print('Running time for broadcast3:', timeit(broadcast3), '(s)')
