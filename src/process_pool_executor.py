import asyncio
import concurrent.futures


# I/O-based task
async def io_task():
    # Perform I/O operations asynchronously using asyncio
    await asyncio.sleep(1)  # Simulating an I/O operation
    print("I/O-based task completed")


# CPU-bound task
def cpu_task(i, data):
    # Perform CPU-intensive computations
    result = data * 2  # Simulating a CPU-bound task
    print("CPU-bound task completed", i)
    return result


async def main():
    # Execute I/O-based task asynchronously
    await io_task()

    # Create a ProcessPoolExecutor for CPU-bound tasks
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Generate data for CPU-bound tasks
        i = [1, 2, 3, 4]
        data = [1, 2, 3, 4]

        # Execute CPU-bound tasks in parallel using the ProcessPoolExecutor
        loop = asyncio.get_event_loop()
        # results = await loop.run_in_executor(executor, cpu_task, data)
        #
        # futures = [loop.run_in_executor(executor, cpu_task, *i)
        #            for i in data]
        # results = await asyncio.gather(*futures)
        # Process the results as needed
        results = executor.map(cpu_task, i, data)

        print("Results:", list(results))


# Run the main function asynchronously
if __name__ == '__main__':
    asyncio.run(main())

