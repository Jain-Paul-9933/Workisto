import {createSlice} from '@reduxjs/toolkit';

const initialState={
    user:null,
};

const  userSlice=createSlice({
    name:'user',
    initialState,
    reducers:{
        setUser:(state,action)=>{
            state.user=action.payload;
        },
        clearUSer:(state,action)=>{
            state.user=null;
        },
    },
});

export const {setUser,clearUSer}=userSlice.actions;

export default userSlice.reducer;