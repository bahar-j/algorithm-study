function solution(answers) {
    var answer = [];
    var student1 = [1,2,3,4,5];
    var student2 = [2,1,2,3,2,4,2,5];
    var student3 = [3,3,1,1,2,2,4,4,5,5];
    var score1 = 0;
    var score2 = 0;
    var score3 = 0;
    var i = 0;
    
    answers.forEach( answer => {
        if(answer == student1[i]){
            score1++;
        }
        
        i++;
        if(i == student1.length){
            i = 0;
        }
    });
    
    i = 0;
    answers.forEach( answer => {
       
        if(answer == student2[i]){
            score2++;
        }
        
        i++;
        if(i == student2.length){
            i = 0;
        }
    });
    
    i = 0;
    answers.forEach( answer => {
       
        if(answer == student3[i]){
            score3++;
        }
        
        i++;
        if(i == student3.length){
            i = 0;
        }
    });
    
    var max = Math.max(score1, score2, score3);

    if (score1 == max) {answer.push(1)};
    if (score2 == max) {answer.push(2)};
    if (score3 == max) {answer.push(3)};
    
    return answer;
}