#include<iostream>
#include<limits>
using namespace std;

class Process{
    public:
        string processName;
        int arrivalTime;
        int burstTime;
        int priority;

        int remainingTime;

		int responseTime;
        int completionTime;
    
        int waitingTime;
        int turnAroundTime;

        void initialize(){
        	remainingTime = burstTime;
        }
};

int main(){
    int numOfProcesses = 5;
    Process processes[numOfProcesses];
    
    processes[0].processName = "T1";
    processes[0].arrivalTime =  0;
    processes[0].burstTime = 4;
    processes[0].priority = 1;
    processes[0].initialize();
    
    
    processes[1].processName = "T2";
    processes[1].arrivalTime =  0;
    processes[1].burstTime = 3;
    processes[1].priority = 2;
    processes[1].initialize();
    

    processes[2].processName = "T3";
    processes[2].arrivalTime =  6;
    processes[2].burstTime = 7;
    processes[2].priority = 1;
    processes[2].initialize();
    
    
    processes[3].processName = "T4";
    processes[3].arrivalTime =  11;
    processes[3].burstTime = 4;
    processes[3].priority = 3;
    processes[3].initialize();
    
    processes[4].processName = "T5";
    processes[4].arrivalTime =  12;
    processes[4].burstTime = 2;
    processes[4].priority = 2;
    processes[4].initialize();
    

   

    cout << "\n" << endl;

    for(int i=0;i<numOfProcesses-1;i++){
        for(int j=i+1;j<numOfProcesses;j++){
            if(processes[j].arrivalTime < processes[i].arrivalTime){
                Process temp = processes[j];
                processes[j] = processes[i];
                processes[i] = temp;
            }
        }
    }

    int currentTime = 0;

    while(true){

    	int currentHighestPriorityIndex = -1;
    	int currentHighestPriority = numeric_limits<int>::max();

    	bool isAllCompleted = true;

    	for(int i=0;i<numOfProcesses;i++){
    		if(processes[i].remainingTime > 0){
    			isAllCompleted = false;
                if(processes[i].arrivalTime <= currentTime){
                    if(processes[i].priority < currentHighestPriority){
                        currentHighestPriority = processes[i].priority;
                        currentHighestPriorityIndex = i;
                    }
                }
    			
    		}
    	}

    	if(isAllCompleted){
    		break;
    	}

		if(processes[currentHighestPriorityIndex].remainingTime == processes[currentHighestPriorityIndex].burstTime){
			processes[currentHighestPriorityIndex].responseTime = currentTime;
		}

    	processes[currentHighestPriorityIndex].remainingTime--;
        currentTime++;

		if(processes[currentHighestPriorityIndex].remainingTime == 0){
			processes[currentHighestPriorityIndex].completionTime = currentTime;
		}
    }


    int sumResponseTime = 0;
    int sumCompletionTime = 0;
    int sumWaitingTime = 0;
    int sumTurnAroundTime = 0;

    for(int n=0;n<numOfProcesses;n++){
        cout << "\nTask " << processes[n].processName << ":\n";
        cout << "Start Time: " << processes[n].responseTime << endl;
        cout << "End Time: " << processes[n].completionTime << endl;
        processes[n].turnAroundTime = processes[n].completionTime - processes[n].arrivalTime;
        processes[n].waitingTime = processes[n].turnAroundTime - processes[n].burstTime;
        cout << "Waiting Time: " << processes[n].waitingTime << endl;
        //cout << "Turn Around Time: " << processes[n].turnAroundTime << "\n" << endl;

        sumResponseTime += processes[n].responseTime;
        sumCompletionTime += processes[n].completionTime;
        sumWaitingTime += processes[n].waitingTime;
        sumTurnAroundTime += processes[n].turnAroundTime;
    }

	cout << "\n\nAverage Response Time for " << (numOfProcesses) << " Processes: " << (float) sumResponseTime/numOfProcesses;
	cout << "\n\nAverage Completion Time for " << (numOfProcesses) << " Processes: " << (float) sumCompletionTime/numOfProcesses;
    cout << "\n\nAverage Waiting Time for " << (numOfProcesses) << " Processes: " << (float) sumWaitingTime/numOfProcesses;
    cout << "\n\nAverage Turn Around Time for " << (numOfProcesses) << " Processes: " << (float) sumTurnAroundTime/numOfProcesses;

    return 0;
}