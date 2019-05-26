SIGNALS' data will all be in a shared folder accessible from all account, but if you would like to upload a cube from CADC here is the procedure:

1) From a terminal:
cadc-data get --verbose CFHT 2309128p

2)From a notebook:
from cadcdata import CadcDataClient
from cadcutils import net
client = CadcDataClient(net.Subject())
c = client.get_file('CFHT', '2309128p', destination='2309128p.fits.fz')