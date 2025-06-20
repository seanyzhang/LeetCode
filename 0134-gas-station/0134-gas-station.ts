function canCompleteCircuit(gas: number[], cost: number[]): number {
    const trackLen: number = gas.length
    let currSurplus: number = 0;
    let totalSurplus: number = 0;
    let startIDX: number = 0;

    for (let i = 0; i < trackLen; i++){
        currSurplus += gas[i] - cost[i]
        totalSurplus += gas[i] - cost[i]

        if (currSurplus < 0) {
            currSurplus = 0
            startIDX = i+1
        } 
    }

    if (totalSurplus < 0 || startIDX == trackLen) {
        return -1;
    } else {
        return startIDX;
    }
};