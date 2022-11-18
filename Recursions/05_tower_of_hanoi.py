def toh(n, from_bar, to_bar, aux_bar):
    if n == 1:
        print(f"Moved disk 1 from {from_bar} to {to_bar}")
    else:
        toh(n-1, from_bar, aux_bar, to_bar)
        print(f"Moved disk {n} from {from_bar} to {to_bar}")
        toh(n-1, aux_bar, to_bar, from_bar)


n = 3
toh(n, "A", "B", "C")
