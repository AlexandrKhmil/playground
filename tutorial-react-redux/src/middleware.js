const begin = { type: 'BEGIN' };
const success = { type: 'SUCCESS' };
const fail = { type: 'FAIL' };

export const fetchPosts = (id) => (dispatch) => {
  dispatch(begin());
}