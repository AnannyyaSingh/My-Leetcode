class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        
        int start=0;
        int end=grid.size()-1;

        long usum=0;
        long bsum=0;
        while(start <= end){

            if(usum <= bsum){
                for(int i=0;i<grid[start].size();i++){
                    usum+=grid[start][i];
                }
                start++;
            }else{
                for(int i=0;i<grid[end].size();i++){
                    bsum+=grid[end][i];
                }
                end--;
            }
        }
        if(usum==bsum){
            return true;
        }
        usum=0;
        bsum=0;

        start=0;
        end=grid[0].size()-1;
        while(start <= end){

            if(usum <= bsum){
                for(int i=0;i<grid.size();i++){
                    usum+=grid[i][start];
                }
                start++;
            }else{
                for(int i=0;i<grid.size();i++){
                    bsum+=grid[i][end];
                }
                end--;
            }
        }
        if(usum==bsum){
            return true;
        }
        return false;
    }
};