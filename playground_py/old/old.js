// GET 'api/algorithm/{id}/execute'
router.get('/:algorithmLink/execute',
  async (req, res) => {
    try {
      const { algorithmLink } = req.params;
      let spawn = require('child_process').spawn,
          py    = spawn('python', [`./python_modules/${algorithmLink}/__init__.py`]),
          data = [1,2,3,4,5,6,7,8,9],
          dataString = '';

      py.stdout.on('data', function(data){
        dataString += data.toString();
      });
      py.stdout.on('end', function(){
        res.status(200).json({data : dataString});
      });
      py.stdin.write(JSON.stringify(data));
      py.stdin.end();
      // const { algorithmLink } = req.params;
      // const fileLocation = `./python_modules/${algorithmLink}/__init__.py`;
      // const python = spawn('python', [fileLocation]);
      // let data = null;
      // python.stdout.on('data', (res) => { 
      //   data = res.toString(); 
      // });
      // python.on('close', (code) => res.status(200).json({ data, code }));
    } catch(error) {
      console.log(error)
      return res.status(500).json({ msg: 'Ошибка выполенния!' });
    }
  }
);

module.exports = router;
