import store from './store';

// Types
export const ADD_TODO = 'ADD_TODO';
export const CHANGE_TODO = 'CHANGE_TODO';

// Action Creators
export const addTodo = (text) => ({ type: ADD_TODO, payload: text, });


export const changeTodo = ({ id, text }) => ({ 
  type: CHANGE_TODO,
  payload: { id, text }
});

// Bind Action Creators
export const bindAddTodo = (text) => store.dispatch(addTodo(text));