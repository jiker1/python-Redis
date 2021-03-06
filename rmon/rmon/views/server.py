from rmon.common.rest import RestView
from rmon.models import Server,ServerSchema

class ServerList(RestView):
    """Redis 服务器列表
    """

    def get(self):
        """获取 Redis 列表
        """
        servers = Server.query.all()
        return ServerSchema().dump(servers,many=True).data

    def post(self):
        """创建 Redis 服务器
        """
        data = request.get_json()
        server,errors = ServerSchema().load(data)
        if errors:
            return errors,400
        server.ping()


class ServerDetail(RestView):
    """ Redis 服务器列表
    """

    method_decorators = (ObjectMustBeExist(Server), )

    def get(self, object_id):
        """获取服务器详情
        """
        data, _ = ServerSchema().dump(g.instance)
        return data

    def put(self, object_id):
        """更新服务器
        """
        schema = ServerSchema(context={'instance': g.instance})
        data = request.get_json()
        server, errors = schema.load(data, partial=True)
        if errors:
            return errors, 400
        server.save()
        return {'ok': True}

    def delete(self, object_id):
        """删除服务器
        """
        g.instance.delete()
        return {'ok': True}, 204server.save()
        return {'ok': True},201


