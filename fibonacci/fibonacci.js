const fib = (n) => {
  if (n === 0) return 0;
  if (n === 1) return 1;

  return fib(n - 1) + fib(n - 2);
};

const test = () => {
  const inputs = [...Array(13).keys()];
  const expectedOutputs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144];

  const message = (testNumber, input, output, expected, header = "") => {
    return `\nTest ${testNumber} ${header}
    \tInput: ${input}
    \tOutput: ${output}
    \tExpected: ${expected}`;
  };

  for (let i = 0; i < inputs.length; i++) {
    input = inputs[i];
    output = fib(input);
    expected = expectedOutputs[i];

    if (output !== expected)
      throw new Error(message(i + 1, input, output, expected, "Wrong Output"));

    console.log(message(i + 1, input, output, expected, "PASSED"));
  }
};

console.time("Total Time");
test();
console.timeEnd("Total Time");

