import thunk from 'redux-thunk';
import { createLogger } from 'redux-logger';
import { createStore, applyMiddleware } from 'redux';
import reducer from './reducer';

const logger = createLogger();

const store = createStore(
  reducer,
  applyMiddleware(thunk, logget),
);

// Store whithout middleware
// import { createStore } from 'redux';
// import reducer from './reducer';

// const store = createStore(reducer);

// export default store;

// Store with initial state
// const store = screateStore(reducer, initialStore);

