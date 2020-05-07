import React from 'react';
import { connect } from 'react-redux';
import { addTodo, changeTodo } from '../../action';

const Component = ({ todos, addTodo, changeTodo }) => {
  return (
    <div>
      <h1>Test redux</h1>
      <button onClick={() => addTodo({ head: 'head', text: 'Text' })}>
        Add
      </button>
      <button onClick={() => changeTodo({ id: 1, text: 'NEW TEXT' })}>
        Change
      </button>
      
      {todos.map((todo, index) =>
        <div key={index}>
          <h4>{todo.head}</h4>
          <p>{todo.text}</p>
        </div>
      )}
    </div>
  );
};

const mapStateToProps = (state, props) => ({
  todos: state.todos,
});

const mapDispatchToProps = (dispatch, props) => ({
  addTodo: (value) => dispatch(addTodo(value)),
  changeTodo: (value) => dispatch(changeTodo(value)),
});

export default connect(mapStateToProps, mapDispatchToProps)(Component);
