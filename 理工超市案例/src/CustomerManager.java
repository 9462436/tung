public class CustomerManager {
    private Customer[]users=new Customer[50];
    private int currCount=0;
    public boolean addUser(Customer cus){
        if(currCount==50)
            return false;
        users[currCount++]=cus;
        return true;
    }
    public boolean loginValidate(String username,String pwd){
        boolean isregister=false;
        for(int i=0;i<currCount;i++){
            isregister=users[i].loginValidate(username,pwd);
            if(isregister)
                break;
        }
        return isregister;
    }
}
