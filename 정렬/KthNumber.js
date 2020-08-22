
function solution(array, commands) {
    var answer = [];
    
    commands.forEach ( cmdArr => {
        var startIdx = cmdArr[0] - 1;
        var endIdx = cmdArr[1];
        var pickedIdx = cmdArr[2] - 1;
        
        var slicedArr = array.slice(startIdx, endIdx);
        slicedArr.sort(function (f, s) { return f-s; });
        //console.log(slicedArr);
        
        answer.push(slicedArr[pickedIdx]);
    });
    
    return answer;
}