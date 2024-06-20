#!/usr/bin/node
exports.esrever = function (list) {
  const listLength = list.length;
  const newList = [];
  for (let i = listLength - 1; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
