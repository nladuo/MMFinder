import numpy as np
import rpyc


class DataBean:
    def __init__(self, _id: str, vec: np.array):
        self._id = _id
        self.vec = vec
        if '\n' in _id:
            raise Exception("_id cannot contain \\n")

        if len(vec.shape) != 1:
            raise Exception("vec must be 1-d vector")

        if vec.dtype != np.float32:
            raise Exception("the dtype of vec must be np.float32")


class SPTAG_RpcSearchClient:

    ALGO_BKT = "BKT"  # SPTAG-BKT is advantageous in search accuracy in very high-dimensional data
    ALGO_KDT = "KDT"  # SPTAG-KDT is advantageous in index building cost,

    DIST_L2 = "L2"
    DIST_Cosine = "Cosine"

    def __init__(self, host, port):
        c = rpyc.connect(host, port)
        c._config['sync_request_timeout'] = None
        self.proxy = c.root

    def search(self, beans: [DataBean], p_resultNum):
        _, vecs = self.__get_meta_and_vec_from_beans(beans)
        vecs_ = vecs.tolist()
        return self.proxy.search(vecs_, p_resultNum)

    def __get_meta_and_vec_from_beans(self, beans: [DataBean]):
        if len(beans) == 0:
            raise Exception("beans length cannot be zero!")

        if len(beans) > 1000:
            raise Exception("cannot add more than 1000 beans at once!")

        dim = beans[0].vec.shape[0]
        meta = ""
        vecs = np.zeros((len(beans), dim))

        for i, bean in enumerate(beans):
            meta += bean._id + '\n'
            vecs[i] = bean.vec

        meta = meta.encode()
        return meta, vecs


if __name__ == "__main__":
    client = SPTAG_RpcSearchClient("127.0.0.1", "8888")
    print("Test Search")
    q = DataBean(_id=f"s{0}", vec=0 * np.ones((10,), dtype=np.float32))
    print(client.search([q], 3))
