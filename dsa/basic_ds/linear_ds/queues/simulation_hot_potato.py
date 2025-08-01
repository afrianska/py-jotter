from queue import Queue


def hot_potato(name_list, num):
    sim_queue = Queue()

    for name in name_list:
        sim_queue.enqueue(name)

    print(name_list)
    print(f"{sim_queue.show()} -> {sim_queue.size()}")

    while sim_queue.size() > 1:
        for i in range(num):
            x = sim_queue.dequeue()
            print(x)
            sim_queue.enqueue(x)

        sim_queue.dequeue()
        print(f"{sim_queue.show()} -> {sim_queue.size()}")

    return sim_queue.dequeue()


x_list = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
print(hot_potato(x_list, 6))
