const solution = (arr) => {
  const setArr = [...new Set(arr)];
  setArr.sort((a, b) => b - a);
};
