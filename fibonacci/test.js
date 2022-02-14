const fib = (n) => {
  if (n === 0) return 0;
  if (n === 1) return 1;

  return fib(n - 1) + fib(n - 2);
};


const fibDP = (n, memo) => {
  if (n in memo) return memo[n];

  if (n === 0) return 0;
  if (n === 1) return 1;

  memo[n] = fibDP(n - 1, memo) + fibDP(n - 2, memo);

  return memo[n];
};

// Test
const n = 45

console.time("Fibonacci without DP");
fib(45)
console.timeEnd("Fibonacci without DP");

console.time("Fibonacci without DP");
fibDP(45, {})
console.timeEnd("Fibonacci without DP");
