import asyncio
import concurrent.futures

l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]


# CPU-bound task
def cpu_task(a, b):
    result = a * b  # Simulating a CPU-bound task
    print(f"{a} * {b} = {result}")
    return result


def executor_with_map():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Generate data for CPU-bound tasks
        results = executor.map(cpu_task, l1, l2)
        print("Results:", list(results))


def executor_with_submit():
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(cpu_task, *l1_l2) for l1_l2 in zip(l1, l2)]

        # Retrieve the results as they become available
        results = [future.result()
                   for future in concurrent.futures.as_completed(futures)]
        print("Results:", list(results))


async def main():
    executor_with_map()
    executor_with_submit()


# Run the main function asynchronously
if __name__ == '__main__':
    asyncio.run(main())
