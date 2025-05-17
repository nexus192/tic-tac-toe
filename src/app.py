from web.controller import Conroller, app
from di.Container import Container
from web.web_mapper import WebMapper
from datasource.data_mapper import SourceMapper

if __name__ == "__main__":

  controller = Conroller(app, Container(), WebMapper(), SourceMapper())
  app.run(host='0.0.0.0', port=5000, debug=True)
