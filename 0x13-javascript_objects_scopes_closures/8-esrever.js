#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight(function (ArrList, current) {
    ArrList.push(current);
    return ArrList;
  }, []);
};
